/*
-------------------------------------------------------
errors3.s
-------------------------------------------------------
Author: Sierra Oliver
ID: 169067437
Email: oliv7437@mylaurier.ca	
Date: 2025-01-30
-------------------------------------------------------
Copies contents of one vector to another.
-------------------------------------------------------
*/
.org 0x1000  // Start at memory location 1000
.text        // Code section
.global _start
_start:

.text // code section
// Copy contents of first element of Vec1 to Vec2
ldr r0, =Vec1
ldr r1, =Vec2
ldr r2, [r0]
str r2, [r1]
// Copy contents of second element of Vec1 to Vec2
add r0, r0, #4 //change to 4 to get next memory location
add r1, r1, #4
ldr r2, [r0]
str r2, [r1]
// Copy contents of second element of Vec1 to Vec2
add r0, r0, #4 //change register to r0
add r1, r1, #4
ldr r2, [r0]
str r2, [r1] //change resgister to r1
// End program
_stop:
b _stop

.data // Initialized data section
Vec1:
.word 1, 2, 3
.bss // Uninitialized data section
Vec2:
.space 6

.end
