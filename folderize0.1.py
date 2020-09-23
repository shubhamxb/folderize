from appJar import gui
import os
import shutil
from pathlib import Path

def exitBox():
    return app.yesNoBox("Close the application?", "Are you sure?")

def press(button):
    if button == "<Delete>":
        app.clearAllEntries(callFunction = False)
    elif button == "Exit":
        exitBox()
        app.stop()
    elif button == "<Escape>":
        app.setStopFunction(exitBox)
        app.stop()

    else:
        path = app.getEntry("f1")
        if path =='':
            app.errorBox("Select a directory", "Please select one")
        else:

            os.chdir(path)

            directories = {
                "Android_app":['.apk'],
            "archive_zip":['.7z','.ace','.dd','.b2z','.crx','.dd','.deb','.gz','.jar','.gzip','.jar','.mht','.r01','.rar','.rpm','.sit','.sitx','.snb','.tar','.tar.gz','.tgz','.zip','.zipx'],
            "audio_files":['.3ga','.aa','.aac','.aax','.aif','.aifc','.aiff','.amr','.ape','.asx','.au','.aup','.awb','.caf','.cda','.flac','.gsm','.iff','.kar','.koz','.m3u8','.m4a','.m4b','.m4p','.m4r','.mid','.midi','.mmf','.mp2','.mp3','.mpa','.mpc','.mpga','.nfa','.oga','.ogg','.oma','.opus','.qcp','.ra','.ram','.rta','.wav','.wma','.xspf'],
            "CAD_files":['.3dm','.3ds','.dwg','.dxf','.max','.obj'],
            "Data_files":['.aae','.adt','.cel','.clp','.cma','.dif','.efx','.fcpevent','.flo','.gbr','.gcw','.ged','.gms','.i5z','.ip','.itl','.keychain','.mtw','.nfi','.nfs','.one','.qb2011','.quickendata','.sdf','.tax2012','.tax2014','.tax2016','.vcf','.vcs','.xmind'],
            "Database_files":['.accdb','.bup','.crypt','.db','.dbf','.mdb','.pdb','.sql'],
            "Developer_files":['.apa','.asc','.asm','.b','.bas','.bet','.bluej','.c','.cbl','.cd','.class','.cod','.cpp','.cs','.d','.def','.dtd','.erb','.fla','.fsproj','.fxc','.h','.hpp','.ise','.iwb','.java','.kv','.lua','.m','.m4','.md','.nib','.o','.owl','.p','.pas','.pb','.pbj','.pbxuser','.pika','.pl','.pwn','.py','.pyw','.qpr','.rc','.resources','.s19','.sb','.sb2','.sh','.sln','.sma','.suo','.swift','.trx','.vbp','.vbproj','.vbx','.vc','.vcxproj','.xap','.xcodeproj','.xib','.xq','.xt','.yml'],
            "Document_files":['.chm','.csk','.doc','.docm','.docx','.dot','.dotx','.eml','.fdxt','.hwp','.log','.m3u','.msg','.odm','.odt','.oxps','.pages','.pages.zip','.pdf','.pmd','.pub','.rtf','.shs','.sxw','.tex','.txt','.vmg','.vnt','.wp5','.wpd','.wps','.xml','.xps'],
            "eBook_files":['.acsm','.apnx','.azw','.azw3','.cbr','.cbt','.cbz','.epub','.fb2','.ibooks','.lit','.lrf','.mbp','.mobi','.opf','.prc','.tcr','.vbk'],
            "Executable_files":['.air','.app','.bat','.cgi','.cmd','.com','.ds','.exe','.gadget','.ipa','.pif','.scr','.vb','.wsf'],
            "Other_Misc_files":['.8bi','.bak','.bbl','.bfc','.bib','.bibtex','.cff','.cmf','.crdownload','.cue','.dao','.dbx','.dem','.dic','.enl','.ens','.enw','.epc','.flt','.fnt','.fon','.gam','.gho','.gpx','.grp','.hex','.hqx','.ics','.idx','.img','.iso','.jad','.kml','.kmz','.map','.marc','.mdf','.mim','.mrc','.msi','.mtb','.nes','.ori','.otf','.part','.pes','.plugin','.ps','.qxp','.rem','.ris','.rom','.sav','.t65','.tec','.tmp','.toast','.torrent','.ttf','.url','.uue','.vcd','.xll'],
            "Paper_layout_files":['.caj','.dtp','.indd','.mdi','.p65','.qxd','.rels'],
            "PLAINTXT": [".txt", ".in", ".out"],
            "PDF": [".pdf"],
            "PY": [".py"],
            "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"], 
            "Presentation_files":['.flipchart','.key','.key.zip','.odp','.pps','.ppsx','.ppt','.pptm','.pptx'],
            "Raster_image_files":['.art','.arw','.avif','.bmp','.cr2','.crw','.dcm','.dds','.djvu','.dmg','.dng','.exr','.flif','.fpx','.gif','.hdr','.heic','.ico','.ithmb','.jp2','.jpeg','.jpg','.kdc','.mac','.nef','.nrw','.orf','.pcd','.pct','.pcx','.pef','.pgm','.pict','.plist','.png','.psd','.pspimage','.raf','.raw','.rwl','.sfw','.sr2','.tga','.thm','.tif','.tiff','.wbmp','.webp','.xcf','.yuv'],
            "Settings_files":['.act','.api','.cdt','.cfg','.dun','.fm3','.gid','.ht','.icm','.inf','.ini','.pkg','.prf','.rdf'],
            "Spread_sheet_files":['.csv','.numbers','.ods','.wk3','.wks','.xlr','.xls','.xlsb','.xlsm','.xlsx'],
            "System_file_formats":['.ani','.bashrc','.bash_history','.bash_profile','.bin','.bud','.cab','.cat','.cpl','.cur','.dat','.deskthemepack','.dev','.dit','.dll','.dmp','.drv','.dvd','.ebd','.ffl','.ffo','.fota','.hiv','.hlp','.htt','.icl','.icns','.iconpackage','.ion','.iptheme','.lnk','.mlc','.nb0','.nfo','.nt','.pck','.pnf','.pol','.prop','.qvm','.reg','.sys'],
            "Vector_image_files":['.ai','.cdr','.cvs','.emf','.emz','.eps','.mix','.odg','.pd','.svg','.vsd','.wmf','.wpg'],
            "Video_files":['.264','.3g2','.3gp','.3gpp','.aep','.amv','.arf','.asf','.avi','.bik','.ced','.cpi','.dav','.dir','.divx','.dvsd','.esp3','.f4v','.flv','.h264','.ifo','.imoviemobile','.m2ts','.m4v','.mepx','.mkv','.mod','.mov','.mp4','.mpeg','.mpg','.mswmm','.mts','.mxf','.nfv','.ogv','.pds','.qt','.rcproject','.rm','.rmvb','.srt','.swf','.thp','.ts','.tvs','.veg','.vep','.vob','.vpj','.vproj','.webm','.wlmp','.wmv','.xesc'],
            "Website_files":['.asp','.aspx','.cer','.cfm','.cfml','.csr','.css','.do','.htm','.html','.js','.json','.jsp','.nzb','.php','.rss','.webloc','.xfdl','.xhtml']
            }

            FLF = {file_format: directory 
            for directory, file_formats in directories.items()
            for file_format in file_formats}

            def folderize():
                for entry in os.scandir():
                    if entry.is_dir():
                        continue
                file_path = Path(entry)
                file_format = file_path.suffix.lower()
                if file_format in FLF:
                    directory_path = Path(FLF[file_format])
                    directory_path.mkdir(exist_ok=True)
                    file_path.rename(directory_path.joinpath(file_path))
                
                for cdir in os.scandir():
                    try:
                        os.rmdir(cdir)
                    except:
                        pass
                
            if __name__ == "__main__":
                folderize()
            app.infoBox('Folder', 'Files Folderized', parent = None)

app = gui ("Folderize", "500x100")
x = app.addDirectoryEntry("f1")
app.enableEnter(press)
app.bindKey("<Delete>",press)
app.bindKey("<Escape>",press)
app.addButtons(["Folderize","Exit"], press)
app.go()