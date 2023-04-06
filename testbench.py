import importlib
from MAxPy import results

def testbench_run(ckt=None, results_filename=None):
    lin = ckt.poly1()
    rst = results.ResultsTable(results_filename, ["mre"])
    print(f">>> testbench init - circuit: {lin.name()}, area: {lin.area}, parameters: {lin.parameters}")
    mre = 0.0
    a = 10
    b = 20
    lin.set_a(a)
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
        if y_out != y_ref:
            print(f"ref {y_ref}, out {y_out}")

    rst.add(lin, {"mre": mre})
    print(f"> mre: {mre:.4f}")
    print(">>> testbench end")
    if mre < 0.1:
        prun_flag = True
    else:
        prun_flag = False
    return prun_flag, lin.node_info


if __name__ == "__main__":
    mod = importlib.import_module(name="poly1_exact.poly1")
    testbench_run(ckt=mod, results_filename="testbench_dev.csv")
