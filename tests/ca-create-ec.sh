#/bin/bash -eu

openssl ecparam -out ZZATCVCA00001.pem -name $1 -genkey
openssl pkcs8 -topk8 -nocrypt -in ZZATCVCA00001.pem -outform DER -out ZZATCVCA00001.pkcs8
cvc-create --role=cvca --type=at --chr=ZZATCVCA00001 --days=365 --sign-key=ZZATCVCA00001.pkcs8 --scheme=$2

openssl ecparam -out ZZATDVCA00001.pem -name $1 -genkey
openssl pkcs8 -topk8 -nocrypt -in ZZATDVCA00001.pem -outform DER -out ZZATDVCA00001.pkcs8
openssl ec -in ZZATDVCA00001.pem -out ZZATDVCA00001.pub -pubout -outform DER 2>/dev/null
cvc-create --role=dv_domestic --type=at --chr=ZZATDVCA00001 --days=180 --sign-key=ZZATCVCA00001.pkcs8 --scheme=$2 --sign-as=ZZATCVCA00001.cvcert --public-key=ZZATDVCA00001.pub

openssl ecparam -out ZZATTERM00001.pem -name $1 -genkey
openssl pkcs8 -topk8 -nocrypt -in ZZATTERM00001.pem -outform DER -out ZZATTERM00001.pkcs8
cvc-create --chr=ZZATTERM00001 --scheme=$2 --sign-key=ZZATTERM00001.pkcs8 --out-cert=ZZATTERM00001.cvreq --req-car=ZZATDVCA00001

cvc-create --role=terminal --type=at --days=60 --sign-key=ZZATDVCA00001.pkcs8 --sign-as=ZZATDVCA00001.cvcert --request=ZZATTERM00001.cvreq
