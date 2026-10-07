movies=['cheli','rrr','sakhi']
shows=['10.00:AM','2.00:PM','6.00:PM']
seats=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5']
bookings=[]
users=[]
price=[150,300,250]
while True:
    print('movie ticket system')
    print("1. ADMIN")
    print("2. USER")
    print("3. EXIT")

    role = int(input("Select role: "))
    if role==1:
        while True:
            print('1.add movie')
            print('2.add shows')
            print('3.add seats')
            print('4.delete movie')
            print('5.delete show')
            print('6.view booking')
            print('7.view movies')
            print('8.exit admin')
            choice=int(input('enter choice'))
            if choice==1:
                movie=input('enter add movie')
                movies.append(movie)
                p=int(input('enter new price'))
                price.append(p)
                print('movie added successfully')
            elif choice==2:
                show=input('enter add show')
                shows.append(show)
                print('show added successfully')
            elif choice==3:
                print('available seats')
                if len(seats)==0:
                    print('no seats available')
                else:
                    for seat in seats:
                        print(seat,end=' ')
                    print()
            elif choice==4:
                if len(movies)==0:
                    print('no movies available')
                else:
                    print('available movies')
                    for i in range(len(movies)):
                        print(i+1,movies[i])
                    movie_no=int(input('enter movie to delete'))
                    if movie_no>=1 and movie_no<=len(movies):
                        movies.pop(movie_no-1)
                        print('deleted movies successfully')
                    else:
                        print('invalid movie number')
            elif choice == 5:
                if len(shows) == 0:
                    print("No shows available.")
                else:
                    print("Shows:")
                    for i in range(len(shows)):
                        print(i + 1, shows[i])
                    show_no = int(input("Enter show number to delete: "))
                    if show_no >= 1 and show_no <= len(shows):
                        shows.pop(show_no - 1)
                        print("Show deleted successfully!")
                    else:
                        print("Invalid show number.")
            elif choice==6:
                if len(bookings)==0:
                    print('no booking')
                else:
                    print('booking')
                    for i in range(len(bookings)):
                        print('booking',i+1)
                        print("User  :", bookings[i][0])
                        print("Movie :", bookings[i][1])
                        print("Show  :", bookings[i][2])
                        print("Seat  :", bookings[i][3])
                        
            elif choice == 7:
                if len(movies)==0:
                    print('movies')
                else:
                    print('no movies')
            elif choice == 8:
                print("Exiting Admin")
                break
            else:
                print("Invalid choice!")
    elif role==2:
        user_name=input("enter user name: ")
        while True:
            print('1.view movies')
            print('2.view shows')
            print('3.book ticket')
            print('4.view booking')
            print('5.billing')
            print('6.exit user')
            choice=int(input('enter choice'))
            if choice==1:
                if len(movies)==0:
                    print('no movies available')
                else:
                    print('available movies')
                    for i in range(len(movies)):
                        print(i+1,movies[i])
            elif choice == 2:
                if len(shows) == 0:
                    print("No shows available.")
                else:
                    print(" SHOWTIMES")
                    for i in range(len(shows)):
                        print(i + 1, shows[i])
            elif choice==3:
                if len(movies)==0:
                    print('no movies available')
                    continue
                if len(shows)==0:
                    print('no shows s available')
                    continue
                if len(seats)==0:
                    print('no seats available')
                    continue
            
                print('movies')
                for i in range(len(movies)):
                    print(i+1,movies[i])
                movie_no=int(input('enter movie num'))
                if movie_no<1 or movie_no>len(movies):
                    print('invallid movie num')
                    continue
                movie = movies[movie_no - 1]
                print("SHOW")
                for i in range(len(shows)):
                    print(i + 1, shows[i])
                show_no = int(input("Select show number: "))
                if show_no < 1 or show_no > len(shows):
                    print("Invalid show number")
                    continue
                show = shows[show_no - 1]
                print("SEATS")
                for seat in seats:
                    print(seat, end=" ")
                print()
                selected_seat = input( "Enter seat number: " )
                if selected_seat not in seats:
                    print("Seat not available.")
                    continue
                seats.remove(selected_seat)
                booking = [user_name,movie,show,selected_seat]
                bookings.append(booking)
                users.append(user_name)  
                print('ticket booked')
                print("User  :", user_name)
                print("Movie :", movie)
                print("Show  :", show)
                print("Seat  :", selected_seat)            
            elif choice == 4:
                found = False
                for booking in bookings:
                    if booking[0] == user_name:
                        print("BOOKING ")
                        print("User  :", booking[0])
                        print("Movie :", booking[1])
                        print("Show  :", booking[2])
                        print("Seat  :", booking[3])
                        found = True
                        if found == False:
                            print("No booking found.")
            elif choice == 5:
                s=0
                if len(bookings)>0:
                    for booking in bookings:
                     if booking[0] == user_name:
                        print("BOOKING ")
                        print("User  :", booking[0])
                        print("Movie :", booking[1])
                        print("Show  :", booking[2])
                        print("Seat  :", booking[3])
                        idx=movies.index(booking[1])
                        print("Price :",price[idx])
                        s+=price[idx]
                    print('Total amount:',s)
                else:
                    print('no booking found')

            elif choice == 6:
                print("exit user")
                break
            else:
                print("invalid choice")
    elif role == 3: 
        print("Thank you for using the system")
        break
    else:
        print("Invalid role!")           

            