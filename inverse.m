% Task 1b

function joint_angle_sets = inverse(cart_cord)
    % input: [x y z]
    % output: [set1 set2 set3 set4] in degrees
    
    L1 = 100.9;
    L2 = 222.1;
    L3 = 136.2;
    x = cart_cord(1);
    y = cart_cord(2);
    z = cart_cord(3);
    
    r = sqrt(x^2+y^2);
    h = sqrt(r^2 + (z-L1)^2);
    D = (h^2 -L2^2-L3^2) / (2*L2*L3);
    E = (h^2 +L2^2-L3^2) / (2*h*L2);
    
    % im not sure how to calculate the rest of the angle sets after
    %   Ive found the first one.
    % But it makes sense that theta3_elbowup = -theta3_elbowdown
    %  and that theta1 rotates 180
    
    %set 1: elbow up
    t1_1 = atan2d(y,x);
    t3_1 = atan2d(sqrt(1-D^2), D);
    t2_1 = atan2d(z-L1, r) - atan2d(sqrt(1-E^2), E);
    set1 = [t1_1 t2_1 t3_1];
    
    %set 2: elbow down
    t1_2 = atan2d(y,x);
    t3_2 = atan2d(sqrt(1-D^2), -D);
    t2_2 = -atan2d(z-L1, r) + atan2d(sqrt(1-E^2), E);
    set2 = [t1_2 t2_2 t3_2];
    
    %set 3: elbow up (rotate 180)
    t1_3 = atan2d(y,x) + 180;
    t3_3 = 180 - t3_1;
    t2_3 = 180 - t2_1;
    set3 = [t1_3 t2_3 t3_3];
    
    %set 4: elbow down (rotate 180)
    t1_4 = atan2d(y,x) + 180;
    t3_4 = 180 - t3_2;
    t2_4 = 180 - t2_2;
    set4 = [t1_4 t2_4 t3_4];
    
    joint_angle_sets = [set1; set2; set3; set4];
end