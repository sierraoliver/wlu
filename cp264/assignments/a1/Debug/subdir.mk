################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../mychar.c \
../mychar_ptest.c \
../powersum.c \
../powersum_ptest.c \
../quadratic.c \
../quadratic_ptest.c 

C_DEPS += \
./mychar.d \
./mychar_ptest.d \
./powersum.d \
./powersum_ptest.d \
./quadratic.d \
./quadratic_ptest.d 

OBJS += \
./mychar.o \
./mychar_ptest.o \
./powersum.o \
./powersum_ptest.o \
./quadratic.o \
./quadratic_ptest.o 


# Each subdirectory must supply rules for building sources it contributes
%.o: ../%.c subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean--2e-

clean--2e-:
	-$(RM) ./mychar.d ./mychar.o ./mychar_ptest.d ./mychar_ptest.o ./powersum.d ./powersum.o ./powersum_ptest.d ./powersum_ptest.o ./quadratic.d ./quadratic.o ./quadratic_ptest.d ./quadratic_ptest.o

.PHONY: clean--2e-

