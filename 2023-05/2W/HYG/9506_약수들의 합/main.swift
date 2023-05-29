//
//  main.swift
//  9506_약수들의 합
//
//  Created by 예강이다 on 2023/05/16.
//

import Foundation

while let n = Int(readLine()!), n != -1 {
    var arr = [Int]()

    for i in 1...n/2 {
        if n % i == 0 {
            arr.append(i)
        }
    }

    if arr.reduce(0, +) == n {
        print("\(n) = \(arr.map { String($0) }.joined(separator: " + "))")
    } else {
        print("\(n) is NOT perfect.")
    }
}

//while let n = Int(readLine()!), n != -1 {
//    var arr = Array(repeating: false, count: n/2 + 1)
//    var str = ""
//    var sum = 0
//
//    for i in 1...n/2 {
//        if n % i == 0 {
//            arr[i] = false
//        }
//    }
//
//}
