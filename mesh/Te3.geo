//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {1, 0, 0, 1.0};
//+
Point(3) = {-1, 0, 0, 1.0};
//+
Point(4) = {0, -1, 0, 1.0};
//+
Point(5) = {0, 1, 0, 1.0};
//+
Circle(1) = {5, 1, 2};
//+
Circle(2) = {5, 1, 3};
//+
Circle(3) = {4, 1, 3};
//+
Circle(4) = {4, 1, 2};
//+
Curve Loop(1) = {2, -3, 4, -1};
//+
Plane Surface(1) = {1};
//+
Show "*";
//+
Physical Surface("S") = {1};
//+
Physical Curve("Ecima") = {2};
//+
Physical Curve("Dcima") = {1};
//+
Physical Curve("Ebaixo") = {3};
//+
Physical Curve("Edir") = {4};
//+
Transfinite Curve {2} = 150 Using Progression 1;
//+
Transfinite Curve {1} = 150 Using Progression 1;
//+
Transfinite Curve {4} = 150 Using Progression 1;
//+
Transfinite Curve {3} = 150 Using Progression 1;
