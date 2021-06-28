import math;

def getCenterAccuracy(res, alpha):
    return math.pi / (10800*math.atan(2*math.tan(0.5*alpha)/res))

def getEdgeAccuracy(res, alpha):
    return math.pi / (10800*math.atan(math.sin(alpha)/(res + math.cos(alpha) - 1)))

def getAccuracies(hres, vres, hfov, vfov):

    hfov_in_radians = math.radians(hfov);
    vfov_in_radians = math.radians(vfov);

    center_accuracy_horizontal = getCenterAccuracy(hres, hfov_in_radians);
    center_accuracy_vertical = getCenterAccuracy(vres, vfov_in_radians);
    edge_accuracy_horizontal = getEdgeAccuracy(hres, hfov_in_radians);
    edge_accuracy_vertical = getEdgeAccuracy(vres, vfov_in_radians);
    
    print("Resolution: {} x {}".format(hres, vres));
    print("HFOV: {} degrees".format(hfov));    
    print("VFOV: {} degrees".format(vfov));
    print("horizontal accuracy: 1 arcmin corresponds to {:.2f} (at center) to {:.2f} (at edge) camera pixels".format(center_accuracy_horizontal, edge_accuracy_horizontal));
    print("vertical accuracy  : 1 arcmin corresponds to {:.2f} (at center) to {:.2f} (at edge) camera pixels".format(center_accuracy_vertical, edge_accuracy_vertical));

# Canon EOS 700D parameters.
getAccuracies(5184, 3456, 60, 40)
