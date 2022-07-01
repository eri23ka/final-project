# final-project
#Final Project
Title: Space Impact 

## Description
Space Impact is a game where the players which are identify as a jet try to prevent the enemy crossing to their territory by firing the opponents that leaves a trail in front of them as they move up and down. 
The enemy moves foward towards the Jet.

The game starts by the player running the file in main.py file
-Players can move up and down using the key:
If Player wants to move up press Arrow Up
If Player wants to move down press Arrow Down

-Players try to maneuver to hit the enemy as it moves, to eliminate the enemy the player must hit the head of the enemy, 
if the players hit the side of the enemy it only weakness it will continue moving, if the enemy gets hit 3 times it will be 
eliminated. 

If enemy collides with the player or enters the player area
-A "game over" message is displayed in the middle of the screen.
-The cycles turn white

## Project Structure
---
The project files and folders are organized as follows:
```
+-- Space Impact              (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
Name                        Assigned                                                                                                                     Email
___________________         _______________________________________________                                                                              ________________
Guillermo Quinteros         JetFighter, Score, Color, Actor, Bullet, Enemy                                                                               qui22003@byui.edu        
Nelson Muchonji B.          Director, Game, Point, Cast, Script                                                                                          bif20001@byui.edu
Erika Ramirez               KeyboardService, MoveActorsAction, Action, HandleCollisionsAction, DrawActorsAction, ControlActorsAction, VideoService       ramirezerika328@gmail.com
