
// Importamos las variables
const pythonCode = document.getElementsByClassName("python_code");

//Añadir elementos de la lista

let list_style_python = ["from","import","pass"];
let list2_style_python = ["class","def"]
let list3_style_python = ["\\(","\\)"]
// Falta por implementa : y **


for (let x = 0; x < list2_style_python.length; x++) {
    for (let i = 0; i < pythonCode.length; i++) {

        // Variables
        let texto = pythonCode[i].innerHTML;
        let palabra_a_buscar = list2_style_python[x];
        let texto_antes = '<span class=\"list2_python_code\">';
        let texto_despues = "</span>";
    
        // Utilizamos una expresión regular para buscar todas las ocurrencias de la palabra
        let nuevo_texto = texto.replace(new RegExp(palabra_a_buscar, 'g'), `${texto_antes}${palabra_a_buscar}${texto_despues}`);
        
        // Exportamos el resultado
        pythonCode[i].innerHTML = nuevo_texto;
    }
}

for (let x = 0; x < list3_style_python.length; x++) {
    for (let i = 0; i < pythonCode.length; i++) {

        // Variables
        let texto = pythonCode[i].innerHTML;
        let palabra_a_buscar = list3_style_python[x];
        let texto_antes = '<span class=\"list3_python_code\">';
        let texto_despues = "</span>";
    
        // Utilizamos una expresión regular para buscar todas las ocurrencias de la palabra
        let nuevo_texto = texto.replace(new RegExp(palabra_a_buscar, 'g'), `${texto_antes}${palabra_a_buscar.replace('\\','')}${texto_despues}`);
        // Exportamos el resultado
        pythonCode[i].innerHTML = nuevo_texto;
    }
}

for (let x = 0; x < list_style_python.length; x++) {
    for (let i = 0; i < pythonCode.length; i++) {

        // Variables
        let texto = pythonCode[i].innerHTML;
        let palabra_a_buscar = list_style_python[x];
        let texto_antes = '<span class=\"list_python_code\">';
        let texto_despues = "</span>";
    
        // Utilizamos una expresión regular para buscar todas las ocurrencias de la palabra
        let nuevo_texto = texto.replace(new RegExp(palabra_a_buscar, 'g'), `${texto_antes}${palabra_a_buscar}${texto_despues}`);
        
        // Exportamos el resultado
        pythonCode[i].innerHTML = nuevo_texto;
    }
}


