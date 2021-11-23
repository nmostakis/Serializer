# XML Movie Collection Converter Documentation
## This converter is capable of converting **_XML_** files, containing movie data, into **_json_**, **_yaml_** or **_CSV_** files.
<hr>

### how to use.
- This Package is written in **_Python 3.10.0_** wich is the **recommended** version to use.
    - to get the correct version of Python go to the website python.org/downloads/
- Once you do the next Step is to get the package installed via **pip**
    - available when finish
- now that you have the Package installed you need to make sure your XML file is **_correctly_** structured
### Examlpe Layout
<hr>

``` 
<collection>
    <genres category="">
        <decade years="">
            <movie favorite="" title="">
                <format multiple=""></format>
                <year></year>
                <rating></rating>
                <description></description>
            </movie>
        </decade>
    </genres>
</collection>
```
-   you may add as many **genres**, **decade** or **movie** _tags_ as you like
    - **IT IS NOT POSSIBLE TO ADD REMOVE OR CHANGE ANY OF THE TAGS ATTRIBUTES OR THEIR ORDER ELSE THE PACKAGE _WON'T BE ABLE TO CONVERT THE FILE_**
    - Although you don't need to fill every detile in this file the _**Tile** and **Rating**_ **must be specified** to convert it into another format.
<hr>

## Logical Function Description
```
import test

test.xmljson("xmlfile.xml","outputfile.json")
test.xmlyaml("xmlfile.xml","outputfile.yaml")
test.xmlcsv("xmlfile.xml","outputfile.csv")

```


- xmljson, xmlyaml and xmlcsv functions from the **test module** take exactly 2 parameters.
=======
- **xmljson**, **xmlyaml** and **xmlcsv** functions from the **test module** take exactly 2 parameters.

    - the first parameter is the file in which you have your **XML** content stored
    - the second parameter is the name of the output file which u want to create
- once either of those functions are called the parameters are checked to have the correct suffix.
    - if the check returns False an error is raised.
- after the first check the XML is converted to an **element Tree object**
    - if this proccess fails a **well-formed error** is raised
        - this means the Parser failed to transform the content for the XML into a Python Object due to incorrect Syntax formaitting either because a tag is not closed or the the attribute is missing quotation marks: **""**
- in the next step a sample element tree object is created to compare the tags and attributes in the Original file
    - if the XML tags or attribute keys are not named exactly as in the Example Layout an XML Content Error is raised
- After the xml object passes all tests a new object for every node containing child nodes is created to store the information in the exact way the xml file is structured and the code itterates through the content of the element tree object to fill the node objects with the necessary information
    - as mentioned befor if any of the **title="" attributes** or **\<rating\> tags** return empty the converter raises an Xml Content Error
- once the itteration of the element tree is finished all the information is stored in the objects and can get parsed into a new file,