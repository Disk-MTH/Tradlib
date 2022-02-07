# Translator

For the overview of the library check [here](https://github.com/Disk-MTH/Translator/blob/master/README.md).

## Make translation files

Translation files must follow JSON formatting (which you can easily find on the internet). The name of the file is not important (it does not serve the identification of the language) on the other hand the extension of the file must correspond to that indicated with the function `set_translation_files_extension` or be ".lang" (by default). To identify the language, a specific key must be present and the name of the language must be associated with it. Here is the minimum configuration for detecting a translation file:
```
example.lang
{
	"language": "english"
}
```
In the example above, after setting the path to the translation file and loading the file, the `get_available_languages` function will return ['english'].

/!\ If this key is missing, the translation file will be not detected!

## Functions

 1. set_translations_files_path(full_path, flat_build, build_architecture)
 
This function is used to define the access path to the translation files  
Args:  
 - full_path (required): The full path to the folder containing the uncompiled translation files:
	 ```python
	full_path="C:\\Users\\some_user\\Desktop\\dev\\Translator"
	 ```
/!\ I recommend putting the path with `"\\"` rather than `"\"` because with `"\"` python can believe that you are trying to put unicode characters. In addition, your paths may or may not end with `"\\"` or `"\"` it will not change anything (`"C:\\Users\\some_user\\Desktop\\dev\\Translator"` and `"C:\\Users\\some_user\\Desktop\\dev\\Translator\\"` are equal)

 - flat_build (optional): Put true if all your translation files are at the root of your project when compiling otherwise leave false.
 
 - build_architecture (optional): The full path for your translation files from the compiled project root:

If you have this structure (bellow) the right argument will be `"resources\\lang"`
```
your_project.exe
│   *.ddl
│   some_required_files  
│
└───resources
	│   some_picture.png
	│   some_sounds.mp3
	│
	└───lang
		│   english.lang

```
/!\ I recommend putting the path with `"\\"` rather than `"\"` because with `"\"` python can believe that you are trying to put unicode characters. In addition, your paths may or may not end with `"\\"` or `"\"` it will not change anything (`"resources\\lang"` and `"resources\\lang\\"` are equal)

2. get_translations_files_path()

This function returns the path of your translation files. If you haven't setup this path with the  `set_translations_files_path` function, this will return the current work directory.

3. set_translation_files_extension(extension)

This function set the extension to use for translations files.  The default extension is ".lang".
Args:  
 - extension (required): The extension you want to set

4. get_translation_files_extension()

This function return your selected extension for translation files. Default is ".lang".

5. load_translations_files()

This function loads your translation files. If you don't have executed `set_translations_files_path`, translations files in the current work directory will be load.

6. get_available_languages()

This function returns the list of available languages. If you don't have executed `load_translations_files`,  this will return an empty list.

7. get_translation(language, keys_list)

This function returns the translation associated with the list of keys given with arguments.  To work, this function requires the execution of `load_translations_files` otherwise you are looking in an empty list.
Args:  
 - language (required): The language (among the list of available languages) in which you want a translation.

 - keys_list (required): The list of keys (in order) allowing access to the desired translation.

For the example bellow:
for  `quit` the right arg is `["text", 0, "quit"]`
for  `title` the right arg is `["text", 1, "title"]`
for  `button_reduce` the right arg is `["button", 0, "button_reduce"]`
```
english.lang
{
	"language": "english",

	"text": [
		{
			"quit": "Quit"
		},
		{
			"title": "Translator"
		}
	],
	
	"button": [
		{
			"button_reduce": "Reduce"
		}
	]
}
```


## License

All the files in this repository are completely free of rights (see the  [license](https://github.com/Disk-MTH/Translator/blob/master/diskmth/LICENSE.txt)) so you can grab the code and do whatever you want with them (just respect the  [license](https://github.com/Disk-MTH/Translator/blob/master/diskmth/LICENSE.txt)).

Thanks for reading and good development!

Disk_MTH