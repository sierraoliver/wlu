/*
-------------------------------------------------------
intro.s
-------------------------------------------------------
Author: Sierra Oliver
ID: 169067437
Email: oliv7437@mylaurier.ca
Date: 2025-01-13
-------------------------------------------------------
Assign to and add contents of registers.
-------------------------------------------------------
*/
.org 0x1000  // Start at memory location 1000
.text        // Code section
.global _start
_start:

mov r0, #9       // Store decimal 9 in register r0
mov r1, #14     // store decimal 14 into register r1
add r2, r1, r0  // Add the contents of r0 and r1 and put result in r2
mov r3, #8     // store decimal 8 into register r3
add r3, r3, r3  // add contents of r3 with itself, and put result in r3
mov r5, #4     // store decimal 4 into register r5
add r4, r5, #5  //add contents of r5 and decimal 5 and put result in r4

// End program
_stop:
b _stop
	