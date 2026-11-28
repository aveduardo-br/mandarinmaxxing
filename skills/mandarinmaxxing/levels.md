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

If the learner later reviews a lesson of a finished level, take its name from that level's map, in the course language.

## HSK 5 and 6

Levels 5 and 6 are experimental: they have a word list in `syllabus/` and no map yet, so you build the map before the overview. Say first, in one line, that this level isn't mapped yet, that preparing it takes several minutes, and that its lessons come out rougher than levels 1 to 4.

Read the level's whole list for this, and build the map with the rules the other maps follow:

- Situations a learner can talk about, not categories. Lessons of about 15 to 25 words.
- Blocks of two to four words that make sentences together, in mixed sizes.
- Look-alike and same-category words in different blocks.
- Core function words early, in a jump start of five lessons at most.

Use the format of `maps/hsk-4.md`, without `Split` lines, and spell every word as the list does, sense numbers included. Write the map to a file a few lessons at a time, then run `python3 check_map.py map-hsk-N.md N <pace>`. It lists every official word the map leaves out, words that aren't in the list, repeated words, and blocks of the wrong size; then the parts of each lesson at the learner's pace and their total, which the overview needs. Fix what it lists and run it again, three times at most. If words are still missing after that, put them in a last lesson of their own rather than leave them out. Where you can't run code, count the words yourself and say the map wasn't checked by script.

Save the map beside the course file as `map-hsk-N.md` and read it from there in later chats; when a plan needs it, give its path on a `MAP` line of `plan.txt`. After HSK 6 there is no next level: only congratulate.
