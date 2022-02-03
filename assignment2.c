/*
    Program Description:
    This program will simulate a security authentication program
    based on an access code containing 4 single-digit integer numbers
    between 0-9. The program should be able to do the following:
    - Enter the code
    - Encrypt and Decrypt the entered code
    - Verify input code
    The program should also be able to show the following menu:
    - Enter any code
    - Encrypt code entered and verify if correct
    - Decrypt code
    - Display the number of times the encrypted code entered matches the
    authorised code (i) successfully (ii) incorrectly
    - Exit program

    Author: Twila Habab C20361521

    Dates
    - Started: 22/02/21
    - Last edited: 03/03/21

    Editor: VSC
    Compiler: mingw

    OS: Windows 10 Home v20H2

    NOTES: 
    array_name[i] == *(array_name + i) 
       subscript           pointer

    reference: assignment1.c
*/
#include <stdio.h>
#include <stdlib.h>

// Declare and assign value for size of arrays that will be used
#define SIZE 4

// Function prototypes
void input(int *, int *, int *, int *);
void encrypt_validate(int *, const int *, int *, int *, int *, int *, int *);
void decrypt(int *, int *, int *);
void show(int *, int *);
void end(int *);

int main(void)
{
    // Declare and assign values
    const int access_code[SIZE] = {4, 5, 2, 3};
    int user_code[SIZE];                            // Array used whenever program asks for user input
    
    int is_code = 0;                                // Boolean if a code is available to be encrypted/decrypted
    int is_encrypted = 0;                           // Boolean for encrypted    
    int is_validated = 0;                           // Boolean for validated
    
    int correct = 0;                                // Amount of times code input is correct
    int incorrect = 0;                              // Amount of times code input is incorrect
    int running = 1;                                // Running is true
    int user_menu;                                  // Variable for choosing the menu

    int invalid_char_input;                         // Used for possible char input from the menu
    int invalid_input = 0;                          // Used to check if user inputs float or char for pin inputs 
    
    do
    {
        // Menu
        printf("\n========================== Welcome to the Security Authentication Program (SAP) ==========================\n\
        \n1. Enter any code\n\
        \n2. Encrypt code entered and verify if correct\n\
        \n3. Decrypt code\n\
        \n4. Display the number of times the encrypted code entered\n\
        \n   matches the authorised code (i) successfully and (ii) incorrectly.\n\
        \n5. Exit program\
        \n======================================================================================================\n");

        // Ask user input for menu
        printf("\nChoose an option by entering the corresponding number from the menu displayed above and hit enter:\n");

        // output buffer
        fflush(stdout);

        // Assign value to user_menu by scanning input
        scanf("%d", &user_menu);

        // USER MENU VALIDATION 
        // if user inputs a char
        if ((invalid_char_input = getchar()) != '\n' && invalid_char_input != EOF)
        {
            // assign user's menu choice to 0 and clears input buffer
            user_menu = 0;
            fflush(stdin);
        } // end if

        // if user inputs a float
        if (user_menu != 1 && user_menu != 2 && user_menu != 3 && user_menu != 4 && user_menu != 5)
        {
            // assign user's menu choice to 0 and clears input buffer
            user_menu = 0;
            fflush(stdin);
        } // end if
        // END OF USER MENU VALIDATION 

        switch (user_menu)
        {
            // Input code (1)
            case 1:
            {
                input(user_code, &is_code, &is_encrypted, &is_validated);

                break;
            } // end case 1


            // Encrypt code and verify (2)
            case 2:
            {
                encrypt_validate(user_code, access_code, &is_code, &is_validated, &is_encrypted, &correct, &incorrect);

                break;
            } // end case 2


            // Decrypt input code (3)
            case 3:
            {
                decrypt(user_code, &is_code, &is_encrypted);

                break;
            } // end case 3


            // Display the number of times the encrypted code entered
            // matches the authorised code successfully / incorrectly
            case 4:
            {
                show(&correct, &incorrect);

                break;
            } // end case 4


            // End program (5)
            case 5:
            {
                printf("\nThank you for using the Security Authentication Program. Hope to see you again.\n");
                
                // Set running to false to exit while loop
                end(&running);

                break;                
            } // end case 5


            // User does not input 1, 2, 3, 4, 5 || user_menu == 0 (from user_menu validation)
            default:
            {
                printf("\nUser input error. You will be brought back to the menu\n");

                break;
            } // end default

        } // end switch

    } while (running == 1); // end do
    
    return 0;
} // end main

// function to input code (array, code_boolean, encryp_boolean, decryp_boolean, valid_boolean)
void input(int *x, int *is_code, int *is_encrypted, int *is_validated)
{
    int invalid, i;

    printf("\nInput a digit:\n");

    // for loop for code input
    for (i = 0; i < SIZE; i++)
    {
        scanf("%d", &*(x + i));

        // check if its more than 9 or less than 0 or if its a char or if its a float
        if(*(x + i) < 0 || *(x + i) > 9 || (invalid = getchar()) != '\n')
        {
            // input buffer
            fflush(stdin);

            printf("\nInvalid input, input not accepted,\n\
            \rplease only input a single digit:\n");

            // Backtrack so that the user can input a new one without getting to the next one
            i = i - 1;         
        }// end if

        else
        {
            // reset boolean values
            *(is_code) = 1;
            *(is_encrypted) = 0;
            *(is_validated) = 0;
        } // end else
        
    } // end for 
    
    printf("\nYour code has been accepted\n");  
    
} // end input()

// function to decrypt code (array, code_boolean, decryp_boolean, encryp_boolean)
void decrypt(int *encrypted_code, int *is_code, int *is_encrypted)
{
    int i;
    int x, y; // placeholders

    // check if there is a code available to decrypt and if menu 2 is chosen
    if (*(is_code) == 1 && *(is_encrypted) == 1)
    {
        // decrementing for loop
        for (i = 0; i < SIZE; i++)
        {
            *(encrypted_code + i) = *(encrypted_code + i) - 1;

            // if value becomes 10
            if (*(encrypted_code + i) == -1)
            {
                *(encrypted_code + i) = 9;
            } // end if

        } // end decrementing for loop

        // swapping for loop
        for (i = 0; i < SIZE; i++)
        {
            // swap 1st with 3rd
            if (i == 0)
            {
                x = *(encrypted_code + i);
                y = *(encrypted_code + (i + 2) );

                *(encrypted_code + i) = y;
                *(encrypted_code + (i + 2) ) = x;
            } // end inner if

            // swap 2 with 4th
            if (i == 1)
            {
                x = *(encrypted_code + i);
                y = *(encrypted_code + (i + 2) );

                *(encrypted_code + i) = y;
                *(encrypted_code + (i + 2) ) = x;
            } // end inner if

        } // end swapping for loop

        printf("\nYour decrypted code:\n");
        // for loop to print code
        for (i = 0; i < SIZE; i++)
        { 
            printf("%d", *(encrypted_code + i));

        } // end for

    } // end if (is_code == 1 && is_encrypted == 1)

    // menu 2 hasn't been chosen 
    else if (*(is_code) == 1 && *(is_encrypted) == 0)
    {
        printf("You have not encrypted your code yet, please choose menu 2 before decrypting\n");
    } // end else if
    
    // no code && not encrypted
    else
    {
        printf("\nThere is no code to decrypt, please choose option 1 to input your code\n");
    } // end else   
    
} // end decrypt()

void encrypt_validate(int *user_code, const int *access_code, int *is_code, int *is_validated, int *is_encrypted, int *right, int *wrong)
{
    int i;
    int x, y; // placeholders
    int same;

   // check if there is code to encrypt
    if (*(is_code) == 1)
    {
        /* START OF ENCRYPTION */
        // check if code has not been encrypted
        if (*(is_encrypted) == 0)
        {
            // swapping for loop
            for (i = 0; i < SIZE; i++)
            {
                // swap 1st with 3rd
                if (i == 0)
                {
                    x = *(user_code + i);
                    y = *(user_code + (i + 2));

                    *(user_code + i) = y;
                    *(user_code + (i + 2)) = x;
                } // end if

                // swap 2 with 4th
                if (i == 1)
                {
                    x = *(user_code + i);
                    y = *(user_code + (i + 2));

                    *(user_code + i) = y;
                    *(user_code + (i + 2)) = x;
                } // end if

            } // end swapping for loop

            // incrementing for loop
            for (i = 0; i < SIZE; i++)
            {
                *(user_code + i) = *(user_code + i) + 1;

                // if value becomes 10
                if (*(user_code + i) == 10)
                {
                    *(user_code + i) = 0;
                } // end if

            } // end incrementing for loop
            
            *is_encrypted = 1; // set encrypted to true

        } // end if (code has not been encrypted)
        /* END OF ENCRYPTION */

        /* START OF VALIDATION */
        // for loop to check every digit
        for (i = 0; i < SIZE; i++)
        {
            if (*(user_code + i) == *(access_code + i))
            {
                same = 1; // set it to true
            } // end if

            else
            {
                same = 0; // set it to false

                break; // exit loop and stop checking 
            } // end else

        } // end outer for

        // check if it has been validated
        if (*(is_validated) == 0)
        {
            if (same == 1) // all digits match
            {
                printf("\nYour code is valid\n");

                *right = *right + 1;
            } // end if
            else
            {
                printf("\nYour code is invalid\n");
                
                *wrong = *wrong + 1;
            } // end else

            // set it to true so that next time this function is called
            // without new code_input, it won't increment correct and incorrect values
            *(is_validated) = 1; 

        } // end if(is_validated == 0)

        // if it has been validated, print out result without incrementing right & wrong variables
        else
        {
            printf("\nYou have already validated your code\n");
            if (same == 1)
            {
                printf("\nYour code is valid\n");
            } // end if

            else
            {
                printf("\nYour code is invalid\n");   
            } // end inner else

        } // end outer else
        /* END OF VALIDATION */

    } // end if (there is code)

    // no code to encrypt
    else
    {
        printf("\nThere is no code to encrypt, please choose option 1 to input your code\n");
    } // end else

} // end encrypt_validate()

// function to display correct and incorrect times (var, var)
void show(int *x, int *y)
{
    printf("\nYou have input the code %d correctly\n", *(x));
    printf("\nYou have input the code %d incorrectly\n", *(y));

} // end show()

// function to exit program
void end(int *end)
{
    *end = 0; // set value to 0 (false)

} // end case()
