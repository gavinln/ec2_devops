import Data.List (nub, sort)

import qualified Data.List as L

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

-- groupItems :: [x] -> [(x, x)]
-- groupItems [x] = map (\l@(x:xs) -> (x, length l)) . L.group . sort $ [x]

groupItems :: (Num a, Ord a) => [a] -> [(a, Int)]
groupItems a = map (\l@(x:xs) -> (x, length l)) . L.group . sort $ a

findKey key = foldr (\(k,v) acc -> if key == k then Just v else acc) Nothing
