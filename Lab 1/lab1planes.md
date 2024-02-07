# Game Plan
If there needs to be repairs:
* No: Move to runway.
* Yes: Move to hanger.

For 7 planes on the waiting runway, if there is a full runway:
* Yes: All planes depart.
  * Queue data structure needs to be used.

For 5 planes in the hanger, if there is a full hanger:
* Yes: Clear waiting runway and all planes to waiting runway
  * Stack data structure needs to be used.

Loop:
1. Clear waiting runway.
2. Move planes from hanger to waiting runway.
3. Clear waiting runway.
