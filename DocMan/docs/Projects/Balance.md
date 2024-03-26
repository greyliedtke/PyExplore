# Balance

## Description
Creating robotics diy kits for education...


### Balance on wheels
1. Balancing on wheels
   1. popular
   2. mobile
   3. easier to control / setup
   4. scalable
   5. [$20 kit](https://www.amazon.com/Platform-Raspberry-MicroBit-Electric-Magnetic/dp/B08WLRR1MQ/ref=sr_1_6?crid=LA4M54Y8ST2J&dib=eyJ2IjoiMSJ9.VSrXtq3hkblEev-dI6L5xzVuZxyQL6kF6lmNTkkc1aWklurRa8yB5MIxT0zHMdeNxD4fjqaVxb5JtNbd1g5KHKmjRAC-V9D0-Cv8srudlzmsatFAj5wAC7259FBrWZrmx4GGxF1QlVL89QUFXPVTllZuBDoG4MA0zgYtwBzNzvRgOTTW9NIsZKtC0mTZo3YtxG9uujbcy2M12Mq-bY5YMq_En8nkG8u763U69OFYLZA.O74MXC3Zt4_n90c763QE1zdmDswqgTZwvSb0YcEjjGU&dib_tag=se&keywords=ball+wheel+arduino&qid=1711387564&sprefix=ball+wheel+arduino%2Caps%2C129&sr=8-6)
   6. Dowels
   7. Accelerometer
   8. Raspberry PI

### Pendulum based balancing
   1. Art and permanent setup. Always plugged in and ready to go.
   2. difficult to control. Also hasn't been done before..
   3. Control feedback
      1. [Slip ring](https://www.amazon.com/GCSLIPRING-conductive-collector-rotating-diameter/dp/B08SBWD8Y4/ref=sr_1_15?crid=3LK44NW92GCDO&dib=eyJ2IjoiMSJ9.XBjgYLurH3Rkiv6zXaa5KhtqxQdhgGw1aorfJxIbj7d3kREkEZi6HyCkLseGn3cTj1Y3QN45Aw6J-n6LrcebfGIo-WPFCUcwqwljqs82zoENizcv-XxRzbNKQWUaj8NUoeyL6W_4M_YqjmA2xId6XoP-K_QjciCI5ONW0UOdhaeb0P9V8O2xnzghcK64stQd2L33QJ2-UOd6wTD6BXfIXC3xicTe0nXXSth8iq6VT_Q.HmvS1B7H1Zppox3AgNFXWQXNFjDqwyKgrYpho72h4fo&dib_tag=se&keywords=4+wire+slip+ring&qid=1711388033&sprefix=4+wire+slip+%2Caps%2C157&sr=8-15)
         1. Calucate based on angle and gravity
         2. wiring will suck and look lame
      2. [Camera](https://www.amazon.com/Smraza-Raspberry-Megapixels-Adjustable-Fish-Eye/dp/B07L2SY756/ref=sr_1_4?crid=QXGHS05LCURU&dib=eyJ2IjoiMSJ9.X1AtVLmkrF_bVGT8D1NyY0-yGtJEJmfhM7ARI6g5QyYCTu-82Hv1a_Q3WZLVcuHY1d2NXBNlTVqbPkzjwow_BtiXvgCPAgzg4JSq8Ii97OYa5IGycQGv1yYmPYsXu3tosFZAZuJ5MwTJNuwH_m5RD_2XeARWO4mZeRkO0FjMlY2UMZMc1NcnXS-hcJzvrxYvF0m0D5_5Bc6xSYJxyuwXl7dR2URkPEG_6pklRCr3Rlg.es0xfaenDZIAm4b6nr_YewR2Pdh3slFq7TT30Uo8_Pc&dib_tag=se&keywords=raspberry+pi+camera+wide+angle&qid=1711395164&sprefix=raspberry+pi+camera+wide%2Caps%2C136&sr=8-4)
         1. get position relative to fixed...
            1. Base 
            2. Joint 
            3. Arm end
         2. adjust servo arm based on postion, and velocity...
            1. angle = f(relative positions)

### Control Kits
1. Matrix control
2. Sensor experimentation
3. PID balance control
4. Angular momentum based balancing
5. Circular motion