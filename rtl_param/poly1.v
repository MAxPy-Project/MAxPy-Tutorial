module poly1(a, b, x, y);
    input signed [7:0] a, b, x;
    output signed [15:0] y;
    wire signed [15:0] p;
    [[MULTIPLIER_TYPE]] #(16, [[MULTIPLIER_K]]) mult1 (a, x, p);
    [[ADDER_TYPE]] #(16, [[ADDER_K]]) sum1 (p, b, y);
endmodule
