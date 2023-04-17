import importlib
from MAxPy import results
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score

def testbench_run(ckt=None, results_filename=None):
    lin = ckt.poly1()
    rst = results.ResultsTable(results_filename, ["mape", "mae", "accuracy"])
    print(f">>> testbench init - circuit: {lin.name()}, area: {lin.area}, parameters: {lin.parameters}")
    y_true = []
    y_pred = []
    for a in range(-128, 128):
        lin.set_a(a)
        for b in range(-128, 128):
            lin.set_b(b)
            for x in range(-128, 128):
                lin.set_x(x)
                lin.eval()
                y_out = lin.get_y()
                if y_out & 0x8000:
                    y_out ^= 0xffff
                    y_out += 1
                    y_out *= -1
                y_ref = int(a*x) + b
                if y_ref != 0:
                    y_true.append(y_ref)
                    y_pred.append(y_out)
                count += 1

    mape = mean_absolute_percentage_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    accuracy = accuracy_score(y_true, y_pred)
    rst.add(lin, {"mape": mape, "mae": mae, "accuracy": accuracy})
    print(f"> mape: {mape:.4f}, mae: {mae:.4f}, accuracy: {accuracy:.4f}")
    print(">>> testbench end")
    if mape < 0.1:
        prun_flag = True
    else:
        prun_flag = False
    return prun_flag, lin.node_info


if __name__ == "__main__":
    mod = importlib.import_module(name="poly1_exact.poly1")
    testbench_run(ckt=mod, results_filename="testbench_dev.csv")
