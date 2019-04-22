
SELECT wbn , species, MAX(num) 
FROM
    (
        SELECT Fishing_and_River.waterbody_name as wbn, 
                (({0} - latitude )^2+({1} - longitude)^2)^0.5 AS dist 
        FROM Fishing_and_River, fish 
        WHERE Fishing_and_River.waterbody_name = fish.waterbody_name 
        ORDER BY dist ASC 
        LIMIT 1 
    ) AS cloeset , fish
WHERE  
    fish.waterbody_name = wbn 
GROUP BY 
    wbn , species
;