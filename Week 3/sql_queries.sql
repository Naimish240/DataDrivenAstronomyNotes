-- select large star
select radius, t_eff from star where radius > 1;

-- select range of hot stars
SELECT
kepler_id, t_eff

FROM
Star

WHERE
t_eff >= 5000 AND t_eff <= 6000;

-- select confirmed exoplanets
SELECT
kepler_name, radius

FROM
Planet

WHERE
status = 'CONFIRMED'
AND radius >= 1
AND radius <= 3;

-- planet stats
SELECT
MIN(radius), MAX(radius), AVG(radius), STDDEV(radius)

FROM
Planet

WHERE
kepler_name is NULL;

-- planets in multi-planet systems
SELECT
kepler_id, COUNT(koi_name)

FROM
Planet

GROUP BY
kepler_id

HAVING
COUNT(koi_name) > 1

ORDER BY 
COUNT(koi_name) desc;

-- system with small planets
SELECT
Star.radius as sun_radius, Planet.radius as planet_radius

FROM
Star, Planet

WHERE
Star.radius / Planet.radius > 1
AND Star.kepler_id = Planet.kepler_id

ORDER BY
Star.radius desc;

-- how many planets for big star
SELECT Star.radius, COUNT(Planet.koi_name)
FROM Star
JOIN Planet on Star.kepler_id = Planet.kepler_id
GROUP BY Planet.kepler_id, Star.radius
HAVING COUNT(Planet.koi_name) > 1 AND Star.radius > 1
ORDER BY Star.radius desc;

-- lonely stars
SELECT Star.kepler_id, Star.t_eff, Star.radius
FROM Star
LEFT OUTER JOIN Planet USING(kepler_id)
GROUP BY Planet.kepler_id, Star.radius, Star.t_eff, Star.radius, Star.kepler_id
HAVING COUNT(Planet.koi_name) = 0
ORDER BY Star.t_eff desc;

-- subquery joint stars and planets
SELECT ROUND(AVG(p.t_eq), 1), MIN(s.t_eff), MAX(s.t_eff)
FROM Star s
JOIN Planet p USING(kepler_id)
WHERE s.t_eff > (
  SELECT AVG(t_eff) FROM Star
);

-- correlated sizes
SELECT p.koi_name, p.radius, s.radius
FROM Star s
LEFT OUTER JOIN Planet p USING(kepler_id)
WHERE s.radius IN 
(SELECT radius FROM Star
ORDER BY radius DESC
LIMIT 5) AND p.koi_name is not null;

