# -*- coding: utf-8 -*-
"""
Defines constants used by the Kademlia DHT network. Where possible naming is
derived from the original Kademlia paper as are the suggested default values.
"""

# Copyright (C) 2012-2013 Nicholas H.Tollervey.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#: Represents the degree of parallelism in network calls.
ALPHA = 3

#: The maximum number of contacts stored in a k-bucket. Must be an even number.
K = 20

#: The default maximum time a NodeLookup is allowed to take (in seconds).
LOOKUP_TIMEOUT = 600

#: The timeout for network connections (in seconds).
RPC_TIMEOUT = 5

#: The timeout for receiving complete message once a connection is made (in
#: seconds). Ensures there are no stale deferreds in the node's _pending
#: dictionary.
RESPONSE_TIMEOUT = 1800  # half an hour

#: How long to wait before an unused k-bucket is refreshed (in seconds).
REFRESH_TIMEOUT = 3600  # 1 hour

#: How long to wait before a node replicates any data it stores (in seconds).
REPLICATE_INTERVAL = REFRESH_TIMEOUT

#: How long to wait before a node checks whether any buckets need refreshing or
#: data needs republishing (in seconds).
REFRESH_INTERVAL = REFRESH_TIMEOUT / 6  # Every 10 minutes.

#: The number of failed remote procedure calls allowed for a contact. If this
#: is equalled or exceeded then the contact is removed from the routing table.
ALLOWED_RPC_FAILS = 5

#: The number of nodes to attempt to use to store a value in the DHT.
DUPLICATION_COUNT = K

#: The duration (in seconds) that is added to a value's creation time in order
#: to work out its expiry timestamp. -1 denotes no expiry point.
EXPIRY_DURATION = -1

#: Defines the errors that can be reported between nodes in the DHT.
ERRORS = {
    # The request simply didn't make any sense.
    1: 'Bad request',
    # The request was parsed but not recognised.
    2: 'Unknown request',
    # The request was parsed and recognised but the node encountered a problem
    # when dealing with it.
    3: 'Internal error',
    # The request was too big for the node to handle.
    4: 'Request too big',
    # Unsupported version of the protocol.
    5: 'Unsupported protocol',
    # The request could not be cryptographically verified.
    6: 'Unverifiable provenance',
    # The key for an item did not match as expected.
    7: 'Key mismatch',
    # The value is superceded (a newer version is known to the node already).
    8: 'Superceded value'
}
