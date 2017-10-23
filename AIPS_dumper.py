import os, sys
def check_in(pipeline_path):
    try:
        opts, arg = getopt.getopt(sys.argv[1:],'i:c:hg',['help','input=','gui'])
        logger.debug(sys.argv[1:])
    except getopt.GetoptError as err:
        logger.error(err)
        sys.exit(2)
    for o,a in opts:
        logger.debug('{0} {1}'.format(o,a))
        if o in ('-i','--input'):
            inputs = headless(a) ## read input file
            inputs['quit'] = 0 ##needed to add to be compatible with GUI
            logger.info('inputs from file: {}'.format(inputs))
        elif o in ('-g','--gui'):
            inputs = GUI_pipeline(pipeline_path).confirm_parameters() ## read input file
            logger.info('inputs from GUI: {}'.format(inputs))
        elif o in ('-h','--help'):
            logger.debug('help will be written soon')
            sys.exit()
        elif o == '-c':
            logger.debug('Executing!')
        else:
            assert False, "rerun with either headless -i or gui" #if none are specifed run GUI
    return inputs
