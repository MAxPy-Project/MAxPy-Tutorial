module poly1(a, b, x, y);
    input signed [7:0] a, b, x;
    output signed [15:0] y;
    assign y = a*x + b;
endmodule
