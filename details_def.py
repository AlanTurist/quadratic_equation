def detail(a, b, c, D):

    if b == 0:
        if (a > 0 and c > 0) or (a < 0 and c < 0):
            print('\n\tThe equation has no solutions..')
        else: 
            print("\nFor finding the solutions of endless incomplete equation we must resolve:")
            print("\n\tx_1,2 = √(-c / a)")
            print("\n\tx_1,2 = +/- √(",-c,'/',a,")")
    
    elif c == 0:
        print("\nFor finding the solutions of incomplete equation we must resolve:")
        print("\n\tx_1 = 0 and x_2 = -b / a")
        print("\n\tx_1 = 0 and x_2 =",-b,"/",a)

    elif D < 0:
        print("\nThe equation has complex solutions..")

    else:
        print("\nFor finding the solutions we must resolve:")
        print("\n\tx_1,2 = (-b -/+ √Δ) / 2*a, Δ = √((b^2) - 4 * a * c)")
        if D == 0:
            print("\n\tThe equation has double solution because Δ = 0:")
            print("\n\tWe must resolve x_1,2 = -b / 2*a")
            print("\n\tx_1,2 =",-b,"/ 2 *",a)
        else:
            print("\n\tΔ = √(",b**2," - 4*",a,"*",c,") = √",D)
            print("\n\tx_1 =",-b,"- √",D,"/ 2 *",a)
            print("\n\tx_2 =",-b,"+ √",D,"/ 2 *",a)
