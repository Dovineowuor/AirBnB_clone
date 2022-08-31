<h1> AirBnB_clone</h1>
<img src="https://github.com/Sgechuki/readme_images/blob/main/header.png" alt="HBNB header">
<a href="https://youtu.be/E12Xc3H2xqo">HBNB Project Overview</a>
<p>The goal of the project is to deploy on your server a simple copy of the <a href="https://alx-intranet.hbtn.io/rltoken/m8g02HcD2ovrl_K-zulYBw">AirBnB website</a>.
You won’t implement all the features, only some of them to cover all fundamental concepts of the ALX Software Engineering higher level programming track.</p>
<p>On completion the web application will be composed of:</p>
  <ul>
    <li>A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)</li>
    <li>A website (the front-end) that shows the final product to everybody: static and dynamic</li>
    <li>A database or files that store data (data = objects)</li>
    <li>An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)</li>
  </ul>
<h2>Final Product</h2>
<img src="https://github.com/Sgechuki/readme_images/blob/main/l1.png" alt="Airbnb clone final product">
<h2>Steps</h2>
<p>The application won't be built all at once, but step by step.
Each step will link to a concept</p>
<h3>The console(command interpreter)</h3>
<p> The command interpreter will be used to manage the objects of our project:</p>
<ul>
  <li>Create a new object (ex: a new User or a new Place)</li>
  <li>Retrieve an object from a file, a database etc…</li>
  <li>Do operations on objects (count, compute stats, etc…)</li>
  <li>Update attributes of an object</li>
  <li>Destroy an object</li>
 </ul>
<img src="https://github.com/Sgechuki/readme_images/blob/main/model.png" alt="the app framework">
<h2>Files and Directories</h2>
<p>
  <ul>
      <li>models directory will contain all classes used for the entire project. A class, called “model” in a OOP
      project is the representation of an object/instance.</li>
      <li>tests directory will contain all unit tests.</li>
      <li>console.py file is the entry point of our command interpreter.</li>
      <li>models/base_model.py file is the base class of all our models. It contains common elements:</li>
      <ul>
        <li>attributes: id, created_at and updated_at</li>
        <li>methods: save() and to_json()</li>
      </ul>
      <li>models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.</li>
  </ul>
 </p>

<h2>OOP</h2>
<ul>
  <li>Create a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances</li>
  <li>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file</li>
  <li>create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel</li>
</ul

### ***Authors:***
              1. [Dovine Owuor] (https://github.com/dovineowuor)
              2. [Seth Gechuki] (https://github.com/sgechuki)
