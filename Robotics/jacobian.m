% Task 3a

function cart_velocities = jacobian(joint_angles, joint_velocities)
    % joint_angles: [t1 t2 t3]
    % joint_velocities: [v1 v2 v3]
    
    L1 = 100.9;
    L2 = 222.1;
    L3 = 136.2;
    t1 = joint_angles(1);
    t2 = joint_angles(2);
    t3 = joint_angles(3);
    q = joint_velocities;
    
    jv_1 = [-sind(t1)*(L3*cosd(t2 + t3) + L2*cosd(t2)); cosd(t1)*(L3*cosd(t2 + t3) + L2*cosd(t2)); 0];
    jv_2 = [-cosd(t1)*(L3*sind(t2 + t3) + L2*sind(t2)); -sind(t1)*(L3*sind(t2 + t3) + L2*sind(t2)); L3*cosd(t2 + t3) + L2*cosd(t2)];
    jv_3 = [-L3*sind(t2 + t3)*cosd(t1); -L3*sind(t2 + t3)*sind(t1); L3*cosd(t2 + t3)];
    jw_1 = [0; 0; 1];
    jw_2 = [sind(t1); -cosd(t1); 0];
    jw_3 = [sind(t1); -cosd(t1); 0];
    
    jv = [jv_1 jv_2 jv_3];
    
    cart_velocities = jv*q';
end