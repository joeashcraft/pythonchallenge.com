import PIL.ImageShow as show
class gthumbViewer(show.UnixViewer):
    def get_command_ex(self, file, **options):
        command = "gthumb "
        executable = "/usr/bin/gthumb"
        return command, executable
show.shutil.which('gthumb')
if show.shutil.which('gthumb'):
    show.register(gthumbViewer, -1)
