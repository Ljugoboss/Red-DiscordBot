from discord import opus
import logging

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

log = logging.getLogger("red.opus_loader")
log.setLevel(logging.DEBUG)

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        log.debug("opus is already loaded")
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            log.debug("managed to load {}".format(opus_lib))
            return
        except OSError:
            log.debug("failed to load {}, trying next one".format(opus_lib))
            pass

    log.debug("Failed to load opus lib")
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
