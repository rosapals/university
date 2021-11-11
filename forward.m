% Task 1a

function cart_cord = forward(joint_angles)
    % input: [q1 q2 q3] in degrees
   
    L1 = 100.9;
    L2 = 222.1;
    L3 = 136.2;
    
    q1 = joint_angles(1);
    q2 = joint_angles(2);
    q3 = joint_angles(3);
    
    D = L3*cosd(q2+q3)+L2*cosd(q2);
    
    % set1
    x = cosd(q1) * D; % x
    y = sind(q1) * D; % y
    z = L1 + L3*sind(q2+q3) + L2*sind(q2); % z
    
    cart_cord = [x; y; z];
end