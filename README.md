## description
https://ficha.n-st-r.xyz/

interactive menu for hotels and restaurants which allows making orders and minimizes physical interactions.
i'm responsible for the menu app itself. this project also includes the [waiter interface](https://github.com/BurlyLlama28/webdev-course-interactive-menu-codebase) to monitor incoming orders. this app started as a part of 3rd term university project.

## 1 lab:
screenshots of responsiveness:
![image](https://user-images.githubusercontent.com/49121161/109878523-13ceac80-7c7d-11eb-94e8-a52f9ea156fd.png)
![image](https://user-images.githubusercontent.com/49121161/109878584-221cc880-7c7d-11eb-95ae-ffe5912e534f.png)
![image](https://user-images.githubusercontent.com/49121161/109878621-2f39b780-7c7d-11eb-9987-1e31f782fe0e.png)
webpack is used as a bundler, it's also responcible for compiling scss

## 2 lab
this is npm project
i'm using `fetch` to pull the menu with pictures from db (rest endpoints).
fetched data is in json format
support for most popular browsers

## 3 lab
we are using react.js for frontend. as you can see, components and other raw files are in src folder. i'm keeping to a single responsibility principle and separating components into different files. the state is managed solely with react hooks and is preserved after reload by utilizing local storage.

## 4 lab
project-specific functionality is the ability to form orders with an interactive menu and to make an order.

## 5 lab
