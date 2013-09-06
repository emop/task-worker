package org.emop.sailing;

import org.python.util.PythonInterpreter;


public class App 
{
    public static void main( String[] args )
    {
    	PythonInterpreter interp = new PythonInterpreter();
    	interp.exec("import sailing.core.commands.run.Command as Runner");
    	interp.exec("Runner().execute('webrobot')");
    }
}
