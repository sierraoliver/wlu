/**
 * -------------------------------------
 * @file  powersum.h
 * file description
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-13
 *
 * -------------------------------------
 */

#ifndef POWERSUM_H_
#define POWERSUM_H_

/**
 * Detect if overflow in power computing of b to power of n
 *
 * @param b - the base
 * @param n - the exponent
 * @return - 1 if overflow happens, 0 otherwise
 */
int power_overflow(int b, int n);

/**
 * Compute and return b to power of n.
 *
 * @param b - the base
 * @param n - the exponent
 * @return - b to the power of n if no overflow happens, 0 otherwise
 */
int mypower(int b, int n);

/**
 * Compute and return the sum of powers.
 *
 * @param b - the base
 * @param n - the exponent
 * @return -  the sum of powers if no overflow happens, 0 otherwise
 */
int powersum(int b, int n);

#endif /* POWERSUM_H_ */
