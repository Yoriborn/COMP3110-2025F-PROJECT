UI MOCKUPS DOCUMENT

Overview
This document explains the UI visualization mockups created for the COMP-3110 Software Engineering group project.
The purpose of the UI is to show how the system displays line mappings between two versions of a source code file.
The visualizations demonstrate the required scenarios:

1. Baseline line mapping (1-to-1)
2. Line splitting (1-to-many)
3. Added, deleted, and changed lines

These examples show how a real interface would present the output of the comparison algorithm developed by the team.

FILES INCLUDED
baseline.png – Shows normal direct line mapping.
split_mapping.png – Shows one-to-many line splitting.
changes.png – Shows added, deleted, and changed lines with visual indicators.

1. BASELINE MAPPING (1 TO 1)
   This case demonstrates when each line in the old file maps directly to a matching line in the new file.
   The UI shows both files side-by-side with connectors linking the matched lines.
   Everything remains unchanged, so no colors or warning indicators are shown.

Purpose:
To show the simplest mapping scenario and the core behavior of the tool.

2. LINE SPLITTING (1 TO MANY)
   This case demonstrates when a single line in the old file expands into multiple lines in the new version.

Example mapping:
1 → 10, 11, 12

The UI shows a branching connector from one old line to multiple new lines.
All split lines are highlighted together to show they originate from one original line.

Purpose:
To represent structural changes in code and fulfill the requirement for split detection.

3. ADDED, DELETED, AND CHANGED LINES
   This case demonstrates visual differences when lines are modified between versions.

Changed lines:
Lines that exist in both versions but have been modified.

Added lines:
Appear only in the new file.

Deleted lines:
Appear only in the old file.

Example mapping:
2 → 11 (changed)
3 → 12 (changed)
5 → - (deleted)

+ → 14 (added)

The UI mockup uses color indicators such as green for added, red for deleted, and another color for changed.

Purpose:
To visually communicate modifications, removals, and insertions between versions.


DESIGN PRINCIPLES USED
High contrast colors for readability.
Simple connectors between related lines.
Consistent color scheme for status indicators.
Clean layout similar to professional diff tools.
Grouping related lines to support understanding.