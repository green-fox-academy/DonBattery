'use strict';

// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

const m_size = 10;

function get_matrix(){
    let mat = []
    for (let y = 0; y < m_size; y++){
        let row = []
        for (let x = 0; x < m_size; x++){
            if (x + y === m_size - 1){ 
                row.push('1')
            }
            else {
                row.push('0')
            }
        }
        mat.push(row)
    }
    return mat
}

console.log(get_matrix())
