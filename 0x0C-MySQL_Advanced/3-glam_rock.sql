-- SQL script that lists all bands with Glam as their main style, ranked by their longevity
SELECT band_name, (if(split, split, 2020) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan  DESC;
