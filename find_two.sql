SELECT trip1.id , {3}.id , (({2}.latitude - {3}.latitude)^2 +({2}.longitude - {3}.longitude)^2)^0.5+trip1.dist AS fin_dist 
FROM
    (
        SELECT {2}.id AS id, (({0} -{2}.latitude)^2+({1}-{2}.longitude)^2)^0.5 AS dist
        FROM {2}
        ORDER BY dist ASC 
        LIMIT 1
    ) AS trip1, {2} ,{3}
WHERE 
    trip1.id = {2}.id 
ORDER BY fin_dist ASC 
LIMIT 1; 
