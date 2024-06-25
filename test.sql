SELECT place, COUNT(*) as count
FROM races
-- WHERE date = (SELECT MAX(date) FROM races)
GROUP BY place;