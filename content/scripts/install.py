async def install_pdr():
    import micropip

    await micropip.install('pdr[pillow]')
