/*
-------------------------------------------------------
l04_t03
-------------------------------------------------------
Author: Sierra Oliver
ID: 169067437
Email: oliv7437@mylaurier.ca
Date: 2025-02-13
-------------------------------------------------------
*/
.org 0x1000 // Start at memory location 1000
.text           // Code section
.global _start
_start:

ldr    r2, =Data    // Store address of start of list
ldr    r3, =_Data   // Store address of end of list
sub    r5, r3, r2   // subtract the start and end of list to get number of bytes
ldr    r6, [r2]     // initialize minimum value
ldr    r7, [r2]     // initialize maximum value

Loop:
ldr    r0, [r2], #4 // Read address with post-increment (r0 = *r2, r2 += 4)
add    r1,r1,r0	   // add value from file to r2
add    r4, r4, #1   // increase the count by 1

cmp    r0, r6       // compare value to minimum 
movlt  r6, r0       // replace min value if value in list is less than min

cmp    r0, r7       // compare value to maximum
movgt  r7, r0       // replace max value if value in list is greater than max

cmp    r3, r2       // Compare current address with end of list
bne    Loop         // If not at end, continue

_stop:
b _stop

.data
.align
Data:
.word   4,5,-9,0,3,0,8,-7,12 // The list of data
_Data: // End of list address

.end
	
	