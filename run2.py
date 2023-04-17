from MAxPy import maxpy
from testbench import testbench_run

circuit = maxpy.AxCircuit(top_name="poly1")
circuit.set_testbench_script(testbench_run)

circuit.set_group("study_no_1")
circuit.set_synth_tool(None)
circuit.set_results_filename("output.csv")
circuit.parameters = {
    "[[MULTIPLIER_TYPE]]": ["LoBa", "Roba", "Drum", "Tosam"],
    "[[MULTIPLIER_K]]": ["1", "2", "3"],
    "[[ADDER_TYPE]]": ["copyA", "eta1", "loa", "trunc0"],
    "[[ADDER_K]]": ["1", "2", "3", "4"],
}
circuit.rtl2py_param_loop(base="rtl_param")
