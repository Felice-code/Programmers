SELECT i.flavor
FROM first_half AS i
JOIN icecream_info AS f ON i.flavor = f.flavor
WHERE i.total_order >= 3000 
AND f.ingredient_type = 'fruit_based'
order by i.total_order desc;