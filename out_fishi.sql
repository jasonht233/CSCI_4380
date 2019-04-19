
SELECT out_fish.out_id , out_fish.fish_id, ((%d - outdoor_recreation.longitude)^2+(%d - outdoor_recreation.latitude)^2)^0.5 AS out_dist
FROM    
    (
        SELECT out_t.id AS out_id , fish_t.id AS fish_id , fish_t.dist AS dist 
        FROM(
                SELECT outdoor_recreation.id AS id , 
                    MIN(((outdoor_recreation.longitude - fishing_and_river.longitude)^2+(outdoor_recreation.latitude-fishing_and_river.latitude)^2)^0.5) AS dist 
                FROM outdoor_recreation , fishing_and_river 
                WHERE outdoor_recreation.county = fishing_and_river.county 
                    AND fishing_pier =True
                GROUP BY outdoor_recreation.id 
            )  AS out_t, 
            (
                SELECT fishing_and_river.id , 
                    ((outdoor_recreation.longitude - fishing_and_river.longitude)^2+(outdoor_recreation.latitude-fishing_and_river.latitude)^2)^0.5  AS dist 
                FROM outdoor_recreation , fishing_and_river
                WHERE outdoor_recreation.county = fishing_and_river.county 
                    AND fishing_pier = True 
            ) AS fish_t
        WHERE 
            out_t.dist = fish_t.dist
    ) AS out_fish 
    , outdoor_recreation , fishing_and_river
WHERE 
    out_fish.out_id = outdoor_recreation.id 

ORDER BY out_dist DESC 
;

    


 




