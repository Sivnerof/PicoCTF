# Enhance!

## Description

Download this image file and find the flag.

* [Download image file](https://artifacts.picoctf.net/c/102/drawing.flag.svg "PicoCTF link to download svg file")

## Hints

* (None)

## Walkthrough

In this challenge we're given a link to download an SVG file named [drawing.flag.svg](./drawing.flag.svg "Flag Drawing SVG"). The image is a large black circle with a small white circle inside, and on the surface holds no *visible* information.

![drawing.flag.svg](./drawing.flag.svg "Flag Drawing SVG")

[SVG's (Scalable Vector Graphics)](https://www.freecodecamp.org/news/svg-basics-what-are-scalable-vector-graphics-and-how-do-you-use-them/ "freeCodeCamp article and lesson on Scalable Vector Graphics") are graphic files that use [XML (Extensible Markup Language)](https://en.wikipedia.org/wiki/XML "Wikipedia article on XML") to define shapes, paths, and text.

Since SVG files are written in code, we can view them in a code editor.

```svg
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   viewBox="0 0 210 297"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.5 (2060ec1f9f, 2020-04-08)"
   sodipodi:docname="drawing.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.69833333"
     inkscape:cx="400"
     inkscape:cy="538.41159"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1872"
     inkscape:window-height="1016"
     inkscape:window-x="48"
     inkscape:window-y="27"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1">
    <ellipse
       id="path3713"
       cx="106.2122"
       cy="134.47203"
       rx="102.05357"
       ry="99.029755"
       style="stroke-width:0.26458332" />
    <circle
       style="fill:#ffffff;stroke-width:0.26458332"
       id="path3717"
       cx="107.59055"
       cy="132.30211"
       r="3.3341289" />
    <ellipse
       style="fill:#000000;stroke-width:0.26458332"
       id="path3719"
       cx="107.45217"
       cy="132.10078"
       rx="0.027842503"
       ry="0.031820003" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.26458332;"
       x="107.43014"
       y="132.08501"
       id="text3723"><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08501"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08942"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3754">i </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09383"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3756">c </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09824"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3758">o </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10265"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3760">C </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10706"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3762">T </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11147"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11588"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3752">c 3 d _ d 0 a 7 5 7 b f }</tspan></text>
  </g>
</svg>
```

If we view the SVG in a code editor (```cat``` will also work and so will ```strings```) we'll see the file metadata and some shape elements being defined, but more importantly we'll see a text element, which is strange because at first glance the image appears to contain no text.

```svg
<text
    xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none stroke-width:0.26458332;"
    x="107.43014"
    y="132.08501"
    id="text3723"><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.08501"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
        id="tspan3748">p </tspan><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.08942"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
        id="tspan3754">i </tspan><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.09383"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
        id="tspan3756">c </tspan><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.09824"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
        id="tspan3758">o </tspan><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.10265"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
        id="tspan3760">C </tspan><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.10706"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
        id="tspan3762">T </tspan><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.11147"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
        id="tspan3764">F { 3 n h 4 n </tspan><tspan
        sodipodi:role="line"
        x="107.43014"
        y="132.11588"
        style="font-size:0.00352781px;line-height:1.25;fill:#ffffffstroke-width:0.26458332;"
        id="tspan3752">c 3 d _ d 0 a 7 5 7 b f }</tspan>
</text>
```

Within the ```<text>``` element, we'll find several ```<tspan>``` elements, these are similar to ```<span>``` in HTML. Within those ```<tspan>``` elements are letters which can not be seen in the image because the ```<tspan>``` elements each have a style attribute with a font size set to ```0.00352781px```.

```
<tspan
    sodipodi:role="line"
    x="107.43014"
    y="132.08501"
    style="font-size:0.00352781px;line-height:1.25;fill:#ffffff stroke-width:0.26458332;"
    id="tspan3748">p</tspan>
```

You can try to increase the font size and resave the file but then you'll find that the letters also overlap eachother because of the closeness of the x and y coordinates defined in the ```<tspan>``` attributes. You can change those too but the easiest way to get the text out would be to just copy and paste them somewhere else.

* p
* i
* c
* o
* C
* T
* F { 3 n h 4 n
* c 3 d _ d 0 a 7 5 7 b f }

After we remove all the text from their ```<tspan>``` elements and put them together we'll finally get our flag.

```picoCTF{3nh4nc3d_d0a757bf}```
