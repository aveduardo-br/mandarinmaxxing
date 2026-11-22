# Levels: finishing one, and HSK 5 and 6

Read this when the learner finishes a level, when `course.md` says `Next: level complete`, or when their level is HSK 5 or 6.

## When a level ends

A level ends when every lesson on the route has all its parts in the **Done** log. After that last part, save as usual with `Next: level complete`. In place of the usual closing line, congratulate the learner in one line and offer the next level.

A later chat that finds `Next: level complete` offers the next level again. If the learner declines, leave the file as it is: reviews and extra practice still work.

If they accept:

1. Read the new level's map, or build it (below).
2. Keep the same `course.md`. Add the finished level's prefix to every **Done** line that has none. Update the level in **Syllabus**, replace **Route** and the **Lessons** list with the new level's, and set **Next** to part 1 of its first lesson. Keep everything else, including the whole **Done** log, so words from the finished level keep coming back.
3. Show the new level's overview as in `setup.md`, leaving out the sentence about lessons, parts and pace, and ask about the route. Save again if it changes.
4. Ask whether to start the first part now or next time, and start only if they say now.

If the learner later reviews a lesson of a finished level, take its name from that level's map.

## HSK 5 and 6

Levels 5 and 6 have a word list in `syllabus/` and no map yet, so you build the map before the overview. Say first, in one line, that this level isn't mapped yet and that preparing it takes a few minutes.

Build it with the rules the other maps follow:

- Situations a learner can talk about, not categories.
- Blocks of two to four words that make sentences together.
- Look-alike and same-category words in different blocks.
- Core function words early, in a short jump start.

Use the format of `maps/hsk-4.md`, without `Split` lines, and spell every word as the list does, sense numbers included. Write the map to a file a few lessons at a time, then run `python3 check_map.py map-hsk-N.md N`. It lists the official words the map leaves out, words that aren't in the list, repeated words, and blocks of the wrong size. Fix what it lists and run it again, three times at most. If words are still missing after that, put them in a last lesson of their own rather than leave them out, and tell the learner the level was built on the spot and may be rougher than levels 1 to 4. Where you can't run code, count the words yourself and say the map wasn't checked by script.

Save the map beside the course file as `map-hsk-N.md` and read it from there in later chats. After HSK 6 there is no next level: only congratulate.
