## A* search algorithm
https://en.wikipedia.org/wiki/A*_search_algorithm

## What Is A Problem?
https://youtu.be/gepUYmWERZA

## Route Finding
https://youtu.be/5lrkPKQwOFE

Note here that we're only looking at how many "steps", or nodes visited, we have to take to go from one node to another. The paths also show a cost value, but we're ignoring those for now. 

## Uniform Cost Search
https://youtu.be/oPe45CJ_o0k

## Uniform Cost Search 1
https://youtu.be/rTddvJ0qd6c

## Uniform Cost Search 2
https://youtu.be/QSjh-ypUhto

## Uniform Cost Search 3
https://youtu.be/bEfXeDfoIY8

## Uniform Cost Search 4
https://youtu.be/zpOf15umlkE

## Uniform Cost Search 5
https://youtu.be/MoyBcrw-n_M


Now that we've added quite a few paths to our map, it can be a bit difficult to follow which paths are being checked at each step.

Starting at 1:30, we are checking the path coming into Craiova from Rimnicu Vilcea, and heading toward either Drobeta (366+120 = 486) or Pitesti (366+318 = 504), both of which are worse than our current best of 418.

After that, we already know the path to get to Drobeta was worse than the path to get to Craiova, so there cannot be a more beneficial path heading to that already explored location.

## On Uniform Cost
https://youtu.be/8xH-3WtswDs

<strong>Uniform Cost search</strong> - expands out equally in all directions, may expend additional effort getting to a fairly direct path to the goal.

<strong>Greedy best-first search</strong> - expands outward toward locations estimated as closer to the goal. If a direct path is available, expends much less effort than Uniform Cost; however, it does not consider any routes in which it may need to temporarily take a further away path in order to arrive at an overall shorter path.

<strong>A* Search</strong> - utilizes both of these - will try to optimize with both the shortest path and the goal in mind. We'll see how this works in the next video. 

## A* Search
https://youtu.be/HNdOFYCtfu4

https://youtu.be/_cPSOQ-sC2k

## A* Search 1
https://youtu.be/yMUqkCzFXts

Note that the path costs here add up together (i.e. Arad >> Sibiu >> Oradea is 140 + 151 = 291), while the estimated distance is given only from the current end node of the path.

https://youtu.be/pfSya9ScozE

Rimnicu Vilcea and Fagaras hardly increased in total value under f\large ff even though they added 80 and 99, respectively, in path cost, as their estimated distance to the goal decreased. Since they are much more in the specific direction of our goal of Bucharest, the search space is much more inclined to expand to them under A*, similar to greedy best-first search.

## A* Search 2
https://youtu.be/gYKBDz2kQJ8

https://youtu.be/kvDVL4G_njI

## A* Search 3
https://youtu.be/DRreaZXn72E

https://youtu.be/Njd5k_I6Sqo

## A* Search 4
https://youtu.be/B_rOIxwLzr8

There are no additional paths with lower totals, so the path with f\large ff of 418 is our shortest path.

## A* Search 5
https://youtu.be/7d4iHfJXPso



