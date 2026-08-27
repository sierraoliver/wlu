/**
 * -------------------------------------
 * @file  powersum.c
 * file description
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-13
 *
 * -------------------------------------
 */

#include "powersum.h"

/**
 * Detect if overflow in power computing of b to power of n
 *
 * @param b - the base
 * @param n - the exponent
 * @return - 1 if overflow happens, 0 otherwise
 */
int power_overflow(int b, int n) {
	int power = 1;
	for (int x = 1;x<=n;x++){
		power*= b;
	}

	if ((b > 0 && n > 0) && power < 0) {
		return 1;
	} else if ((b < 0 && n < 0) && power > 0) {
		return 1;
	} else {
		return 0;
	}
}

/**
 * Compute and return b to power of n.
 *
 * @param b - the base
 * @param n - the exponent
 * @return - b to the power of n if no overflow happens, 0 otherwise
 */
int mypower(int b, int n) {

	if (power_overflow(b, n) == 1) {
		return 0;
	} else {
		int power = 1;
		for (int x = 1;x<=n;x++){
			power*= b;
		}
		return power;
	}

}

/**
 * Compute and return the sum of powers.
 *
 * @param b - the base
 * @param n - the exponent
 * @return -  the sum of powers if no overflow happens, 0 otherwise
 */
int powersum(int b, int n) {
	int sum = 0;

	if (power_overflow(b,n) ==1){
		return 0;
	}

	else{
		for (int x = 0; x <= n; x++) {
			int power = 1;
			for (int y =1;y<=x;y++){
				power*=b;
			}
			sum+= power;
		}
		
		if ((b>0 && n>0) && sum<0){
			sum = 0;
		}
		else if ((b<0 && n<0) && sum >0){
			sum = 0;
		}

		return sum;
	}

}
