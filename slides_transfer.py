import pypandoc


def write_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


# With an input file: pypandoc will infer the input format from the filename
output = pypandoc.convert_file('Presentation.md'', to='rst')
write_file('Presentation.rst'', output)

# You can make a slidy HTML slide deck
slides_HP = pypandoc.convert_file('Presentation.md', to='slidy', extra_args=['-s'])

# And specify style with a css file, e.g. https://github.com/alblaine/countess
slides_HP = pypandoc.convert_file('Presentation.md', to='slidy', extra_args=['-s', '--css=style.css'])

# Another option is to make a dzslides HTML slide deck
slides_HP = pypandoc.convert_file('Presentation.md', to='dzslides', extra_args=['-s'])

# And now with a css style: https://gist.github.com/bjin/2264634
slides_HP = pypandoc.convert_file('Presentation.md', to='dzslides', extra_args=['-s', '--css=slide.css'])

# You can also make a revealjs HTML slide deck
slides_HP = pypandoc.convert_file('Presentation.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js'])

# Try the sky revealjs theme
slides_HP = pypandoc.convert_file('Presentation.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js', '-V', 'theme=sky'])

# Try the moon revealjs theme
slides_HP = pypandoc.convert_file('Presentation.md', to='revealjs', extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js', '-V', 'theme=moon'])

write_file('Presentation_HPL.html', slides_HP)
