//
//  main.swift
//  이상한 문자 만들기
//
//  Created by 예강이다 on 2023/05/20.
//

import Foundation

let s = "try hello world"

var result = ""
var cnt = 0

for i in s {
    if cnt % 2 == 0 {
        result.append(String(i.uppercased()))
    } else {
        result.append(String(i.lowercased()))
    }
    cnt += 1
    
    if i == " " {
        cnt = 0
    }
}
print(result)
