import sys

def get_argv_dict() -> dict:
    argv_dict = {}
    for key in sys.argv:
        if key.startswith('-'):
            _index = sys.argv.index(key)
            if len(sys.argv) > _index + 1:  # and sys.argv[_index + 1].isdigit()
                argv = sys.argv[_index + 1]
                if not argv.startswith('-'):
                    argv_dict[key] = int(argv) if argv.isdigit() else argv
                    continue
            argv_dict[key] = True
    return argv_dict
