//
//  main.swift
//  삼총사
//
//  Created by 예강이다 on 2023/05/20.
//

import Foundation

let number = [-3, -2, -1, 0, 1, 2, 3]

var num = number.sorted()
var result = 0

for i in 0..<num.count {
    for j in i+1..<num.count {
        for k in j+1..<num.count {
            if num[i] + num[j] + num[k] == 0 {
                result += 1
            }
        }
    }
}
print(result)
