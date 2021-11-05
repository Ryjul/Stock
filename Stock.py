
i=0
while i in range(0,100):
    print ("Dilution Calculator")
    
    while i >=0:
        try:
            conc_input = float(input("Enter final concentration (mM): "))
            mole_input = float(input("Enter molecular mass (g/mol): "))
            mass_input = float(input("Enter mass (mg): "))
        except ValueError:
            print('Invalid response')
        else:
            break

    liters_to_micro = 1000000
    concentration = conc_input / 1000
    grams = mass_input / 1000
    moles = grams / mole_input
    liters = moles / concentration
    microliters = liters * liters_to_micro

    print("Add" , round(microliters , 2), "uL to" , mass_input, "mg of sample to make a" , conc_input, " mM solition.")
    is_it = input('Continue? (y/n)')
    if is_it == 'y' or is_it == 'Y':
        i += 1
        print()
            
    else:
        quit()

    

    
